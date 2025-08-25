// Odoo’s AMD-style module definition.
// first argument - templatename
// second argument ([ ... ]) is an array of dependencies that this module needs.
// third argument is a callback function that will run when all dependencies are loaded.
// QWeb → layout → assets → registry → OWL render.
odoo.define('reimbursement_tracking.HelloComponent', [ 
    '@odoo/owl',
    '@web/core/registry',
], function(require) {
    "use strict";

    const { Component, useState } = require("@odoo/owl");
    const { registry } = require("@web/core/registry");

    class HelloComponent extends Component {
        static template = "reimbursement_tracking.HelloComponent";  //Which XML template should I use when rendering this component? it looks at its static template property

        setup() {
            this.state = useState({ count: 0 });
        }

        increment() {
            this.state.count++;
        }
    }

    registry.category("public_components").add("reimbursement_tracking.HelloComponent", HelloComponent);

    return HelloComponent;
});
