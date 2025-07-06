class LLMBenchmarkDashboard {
    constructor() {
        this.generalData = null;
        this.complicatedData = null;
        this.generalSort = { column: 'overall_score', direction: 'desc' };
        this.complicatedSort = { column: 'overall_score', direction: 'desc' };
        this.metricDisplayNames = {
            comprehension_score: 'Comprehension',
            structure_score: 'Coherence',
            prose_style_score: 'Style',
            creativity_score: 'Creativity',
            depth_score: 'Depth',
            helpfulness_score: 'Helpfulness',
            overall_score: 'Overall'
        };
        this.modelLinks = {
            'Monomer-24B-Writer': 'https://huggingface.co/zake7749/Monomer-24B-Writer-Preview',
            'Monomer-8B-Writer': 'https://huggingface.co/zake7749/Monomer-8B-Writer-Preview'
        };
        this.init();
    }

    async init() {
        this.showLoading(true);
        await Promise.all([
            this.loadData('data/all-scores.json', 'general'),
            this.loadData('data/complicated-writing-scores.json', 'complicated')
        ]);
        this.renderTable('general');
        this.renderTable('complicated');
        this.showLoading(false);
    }

    async loadData(path, type) {
        try {
            const response = await fetch(path);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            if (type === 'general') {
                this.generalData = data;
            } else {
                this.complicatedData = data;
            }
        } catch (error) {
            console.error(`Error loading ${type} data:`, error);
            this.showError(`Failed to load ${type} benchmark data. Please ensure the JSON file exists in the correct directory.`);
        }
    }

    renderTable(type) {
        const data = type === 'general' ? this.generalData : this.complicatedData;
        const sortState = type === 'general' ? this.generalSort : this.complicatedSort;
        const tableContainer = document.getElementById(type === 'general' ? 'generalTable' : 'complicatedTable');
        if (!data) return;

        const models = Object.keys(data);
        const metrics = Object.keys(data[models[0]]);

        const tableHTML = `
            <table>
                <thead>
                    <tr>
                        <th class="sortable${sortState.column === 'model' ? ' sort-' + sortState.direction : ''}" data-type="${type}" data-column="model">Model</th>
                        ${metrics.map(metric => `
                            <th class="sortable${sortState.column === metric ? ' sort-' + sortState.direction : ''}" data-type="${type}" data-column="${metric}">${this.metricDisplayNames[metric] || metric}</th>
                        `).join('')}
                    </tr>
                </thead>
                <tbody>
                    ${this.getSortedTableData(data, sortState, metrics).map(row => {
                        const isMonomer = this.modelLinks[row.model];
                        return `
                        <tr${isMonomer ? ' class="highlight-row"' : ''}>
                            <td class="model-cell">${isMonomer ? `<a href="${this.modelLinks[row.model]}" target="_blank" rel="noopener" class="model-link">${row.model}</a>` : row.model}</td>
                            ${metrics.map(metric => `
                                <td class="score-cell">${this.formatScore(row[metric])}</td>
                            `).join('')}
                        </tr>
                    `; 
                    }).join('')}
                </tbody>
            </table>
        `;

        tableContainer.innerHTML = tableHTML;
        this.setupTableSorting(type);
    }

    getSortedTableData(data, sortState, metrics) {
        const models = Object.keys(data);
        let tableData = models.map(model => ({
            model,
            ...data[model]
        }));

        // Apply current sorting
        if (sortState.column) {
            tableData.sort((a, b) => {
                let aVal = a[sortState.column];
                let bVal = b[sortState.column];
                if (sortState.column === 'model') {
                    aVal = aVal.toLowerCase();
                    bVal = bVal.toLowerCase();
                }
                if (aVal < bVal) return sortState.direction === 'asc' ? -1 : 1;
                if (aVal > bVal) return sortState.direction === 'asc' ? 1 : -1;
                return 0;
            });
        }
        return tableData;
    }

    formatScore(value) {
        if (typeof value === 'number') {
            return value.toFixed(2);
        }
        return value;
    }

    setupTableSorting(type) {
        const tableContainer = document.getElementById(type === 'general' ? 'generalTable' : 'complicatedTable');
        const headers = tableContainer.querySelectorAll('th.sortable');
        headers.forEach(header => {
            header.addEventListener('click', () => {
                const column = header.dataset.column;
                this.handleSort(type, column, header);
            });
        });
    }

    handleSort(type, column, headerElement) {
        const sortState = type === 'general' ? this.generalSort : this.complicatedSort;
        // Update sort direction
        if (sortState.column === column) {
            sortState.direction = sortState.direction === 'asc' ? 'desc' : 'asc';
        } else {
            sortState.column = column;
            sortState.direction = 'asc';
        }
        // Update header classes
        const tableContainer = document.getElementById(type === 'general' ? 'generalTable' : 'complicatedTable');
        tableContainer.querySelectorAll('th.sortable').forEach(th => {
            th.classList.remove('sort-asc', 'sort-desc');
        });
        headerElement.classList.add(`sort-${sortState.direction}`);
        // Re-render table with new sorting
        this.renderTable(type);
    }

    showLoading(show) {
        const loading = document.getElementById('loading');
        if (show) {
            loading.classList.remove('hidden');
        } else {
            loading.classList.add('hidden');
        }
    }

    showError(message) {
        const loading = document.getElementById('loading');
        loading.innerHTML = `
            <div class="no-data">
                <i class="fas fa-exclamation-triangle"></i>
                <p>${message}</p>
            </div>
        `;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new LLMBenchmarkDashboard();
}); 