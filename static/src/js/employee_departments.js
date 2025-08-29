odoo.define('reimbursement_tracking.employee_departments', [], function (require) {
    document.addEventListener('DOMContentLoaded', function () {

        let input = document.getElementById('dept-search');
        let items = document.querySelectorAll('.department-item');

        if (input) {
            input.addEventListener('input', function () {
                let query = input.value.toLowerCase();
                items.forEach(item => {
                    let text = item.textContent.toLowerCase();
                    item.style.display = text.includes(query) ? '' : 'none';
                });
            });
        }
    });
});
