/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class Employeeprofile extends Component {
    setup() {
        this.orm = useService("orm");
        this.state = useState({
            employees: [],
            filteredEmployees: [],
            totalEmployees: 0,
            totalDepartments: 0,
            missingContacts: 0,
            currentPage: 1,
            pageSize: 5,
        });

        onWillStart(async () => {
            let employees = await this.orm.searchRead(
                "employee.profile",
                [],
                ["name", "job_position", "department", "work_email", "work_mobile", "employee_code"]
            );

            let departments = new Set(employees.map(e => e.department[1])); 
            let missingContacts = employees.filter(e => !e.work_email || !e.work_mobile).length;

            this.state.employees = employees;
            this.state.filteredEmployees = employees;
            this.state.totalEmployees = employees.length;
            this.state.totalDepartments = departments.size;
            this.state.missingContacts = missingContacts;
        });
    }

    get paginatedEmployees() {
        let start = (this.state.currentPage - 1) * this.state.pageSize;
        let end = start + this.state.pageSize;
        return this.state.filteredEmployees.slice(start, end);
    }

    get pageCount() {
        return Math.ceil(this.state.filteredEmployees.length / this.state.pageSize);
    }

    onSearch(ev) {
        let query = ev.target.value.toLowerCase();

        const clean = str => (str ? str.toLowerCase().replace(/[^a-z0-9]/gi, '') : '');

        let cleanQuery = clean(query);

        this.state.filteredEmployees = this.state.employees.filter(e =>
            clean(e.name).includes(cleanQuery) ||
            clean(e.job_position).includes(cleanQuery) ||
            clean(e.department && e.department[1]).includes(cleanQuery) ||
            clean(e.work_email).includes(cleanQuery) ||
            clean(e.employee_code).includes(cleanQuery)
        );

        this.state.currentPage = 1;
    }

    goToPreviousPage() {
        if (this.state.currentPage > 1) {
            this.state.currentPage -= 1;
        }
    }

    goToNextPage() {
        if (this.state.currentPage < this.pageCount) {
            this.state.currentPage += 1;
        }
    }
}

Employeeprofile.template = "reimbursement_tracking.Employeeprofile";
registry.category("actions").add("employee_profile_action", Employeeprofile);
