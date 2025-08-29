odoo.define('reimbursement_tracking.employee_departments', [], function (require) {
    "use strict";

    document.addEventListener('DOMContentLoaded', function () {
        let input = document.getElementById('dept-search');
        let items = document.querySelectorAll('.department-item');

        // helper: clean strings (remove special characters, keep alphanumeric)
        const clean = str => (str ? str.toLowerCase().replace(/[^a-z0-9]/gi, '') : '');

        function doSearch() {
            let query = clean(input.value);
            items.forEach(item => {
                let text = clean(item.textContent);
                item.style.display = text.includes(query) ? '' : 'none';
            });
        }

        if (input) {
            input.addEventListener('input', doSearch);
            let searchBtn = document.querySelector('.search_button');
            if (searchBtn) {
                searchBtn.addEventListener('click', doSearch);
            }
        }
    });
});
