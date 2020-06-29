# Rapti CRM v1.0

Customizations targetted for Rapti Gas Pvt Ltd by Atmark IT Solutions

# Rapti Gas CRM Extended Models for specific requirement fulfillment.

### Augments the existing ERPNext CRM Module with specialized ones

---

- Adds a new Domain Rapti CRM for localizing changes within the app.
- Allows for automated/kanban centric fulfillment of CRM requirements by Rapti.
- Allows for recording of purchase of new empty Cylinders.
- Allows for addition of gas purchase order
- Allows for cylinder retrieval
- Allows for sales of stocked cylinders.

---

### New DocTypes Introduced.

---

- Purchase of New Empty Cylinders
- Gas Purchase Order
- Cylinder Retrieval
- Cylinder Sales

---

### Installation

Navigate to your site's bench directory, use the following commands 
    
    bench get-app rapti_crm https://github.com/coderkoala/rapti_crm
    bench install-app rapti_crm
    bench migrate
    
In case of a multi tenant system, simply add
    
    --site <Your_Site_Name>

---

#### License

Copyright © 2020 [Nobel Dahal](https://nobeldahal.com.np)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Made in behalf of Rapti Gas Limited Pvt. Ltd.