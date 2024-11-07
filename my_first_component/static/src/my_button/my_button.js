/** @odoo-module */
import { Component } from '@odoo/owl';
import { registry } from '@web/core/registry';
import { standardActionServiceProps } from "@web/webclient/actions/action_service";

class MyButton extends Component {
    static template = "my_first_component.MyButtonTemplate";
    static props = {
        ...standardActionServiceProps
    }

    onClick() {
        alert("Hello from MyButton!");
    }
}

registry.category("actions").add('my_button_client', MyButton);

