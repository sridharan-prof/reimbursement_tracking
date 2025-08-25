odoo.define('reimbursement_details.employee_departments', [], function (require) {
    document.addEventListener('DOMContentLoaded', function () {

        const input = document.getElementById('dept-search');
        const items = document.querySelectorAll('.department-item');

        if (input) {
            input.addEventListener('input', function () {
                const query = input.value.toLowerCase();
                items.forEach(item => {
                    const text = item.textContent.toLowerCase();
                    item.style.display = text.includes(query) ? '' : 'none';
                });
            });
        }
    });
});
