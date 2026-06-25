# answer4.py
# - exam2
# robert.jiranek@gmail.com

import sys
from  flask import Flask, render_template, request, redirect, url_for

from lib.lib_database import *

database_connect_exam02={
        "database": "exam2",
        "host":"192.168.56.1",
        "port":"5432",
        "username":"robert",
        "userpwd":"central"
        }

cfg_web_main = {
 "project_name":"exam2 / answer4"
,"project_page_name":"/"
}

cfg_web_pages = [
 {"page_url":"/","page_name":"home","page_title":"home page for this project","location":"topmenu"}
,{"page_url":"/databaseinfo","page_name":"database info","page_title":"informations about database connection","location":"buttonmenu"}
,{"page_url":"/items","page_name":"items","page_title":"select products","location":"topmenu"}
,{"page_url":"/add_product","page_name":"add product","page_title":"add product in my project","location":"topmenu"}
]

form_add_item=f"""
<form method="post" name="add_product" class="niceform" action="">
    <label for="name">name:</label>
        <input type="text" 
               name="name" id="name"
               value="<<name_value>>">
    <label for="description">description:</label> 
        <textarea name="description" id="description" rows="5" cols="10"><<description_value>></textarea>
    <label for="price">price:</label>
        <input type="number" 
               name="price" id="price" step="1"
               value="<<price_value>>">                
    <button type="submit" >submit</button>
</form>
"""

class Htmlmachine():
    def __init__(self):
        pass
    def html_menu_get(self, menu_type="topmenu", menu_list: list = cfg_web_pages):
        menu_type = menu_type.lower()
        menu = ""
        for row in menu_list:
            if menu_type in row["location"].lower():
                row_menu = f'<a href="{row["page_url"]}">{row["page_name"]}</a>'
                if menu_type == "topmenu":
                        row_menu = f'<li>{row_menu}</li>'
                menu = f'{menu}{row_menu}\n'
        return menu
    def page_name_get(self, page_url, page_list=cfg_web_main):
        for page in page_list:
            if page["page_url"] == page_url:
                return page["page_name"]
        return ""
    def html_message_set(self, message: str = "", messagetype: str = "message"):
        if message:
            mtype = ""
            if messagetype.lower() != "message":
                mtype = f"<strong>{messagetype.upper()}</strong>:"
            self.message_detail = {"message_type": f"{messagetype.lower()}", "message_message": f"{message}",
                              "message_formated": f'<div class="message_{messagetype.lower()}">{mtype} {message}</div>'}
        else:
            self.message_detail = {"message_type": "", "message_message": "", "message_formated": ""}
        return self.message_detail
    def table_list_genertor(self, data):
        if len(data) == 0:
            self.message_detail  = self.html_message_set("data was not loaded", "warning")
            return ""

        htmlcode = f"<table>\n"
        htmlcode = f"{htmlcode}  <tr>\n"
        for tabheader in data[0].keys():
            htmlcode = f"{htmlcode}    <th>{tabheader}</th>\n"
        htmlcode = f"{htmlcode}  </tr>\n"

        for row in data:
            htmlcode = f"{htmlcode}  <tr>\n"
            for ikey, ivalue in row.items():
                htmlcode = f"{htmlcode}    <td>{ivalue}</td>\n"

            htmlcode = f"{htmlcode}  </tr>\n"

        htmlcode = f"{htmlcode}</table>\n"
        return htmlcode
    def table_detail_genertor(self, data):
        if len(data) == 0:
            self.message_detail = self.html_message_set("data was not loaded", "warning")
            return ""

        htmlcode = f"<table>\n"

        for ikey, ivalue in data.items():
            htmlcode = f"{htmlcode}  <tr>\n"
            htmlcode = f'{htmlcode}  <th class="detail">{ikey}</th><td class="detail">{ivalue}</td>\n'
            htmlcode = f"{htmlcode}  </tr>\n"

        htmlcode = f"{htmlcode}</table>\n"
        return htmlcode

try:
    # connect to database
    examdb=database()
    examdb.connect(connect_string=database_connect_exam02)
    # examdb.sys_database_info(onscreen = True)

    myhtml = Htmlmachine()

    app = Flask(__name__)

    message_detail=""

    @app.route("/")
    def root():
        cfg_web_main["project_page_name"] = myhtml.page_name_get(page_url=request.path, page_list=cfg_web_pages)
        myhtml.message_detail = myhtml.html_message_set()
        html_body = f'flask started on: <a href="{request.url_root}">{request.url_root}<a/>'
        html_body = f"{html_body}<div><ul>{myhtml.html_menu_get(menu_type="topmenu", menu_list=cfg_web_pages)}</ul></div>"
        return render_template("rjdesign.html"
                               , html_project_detail=cfg_web_main
                               , html_body=html_body
                               , html_message_detail=myhtml.message_detail
                               , html_menu_top=myhtml.html_menu_get(menu_type="topmenu", menu_list=cfg_web_pages)
                               , html_menu_button=myhtml.html_menu_get(menu_type="buttonmenu", menu_list=cfg_web_pages)
                               )

    @app.route("/items", methods=["GET", 'POST'])
    def items():
        cfg_web_main["project_page_name"]=myhtml.page_name_get(page_url=request.path, page_list=cfg_web_pages)
        myhtml.message_detail = myhtml.html_message_set()
        html_body = myhtml.table_list_genertor(examdb.sqlcommand_execute('select * from items order by name'))
        return render_template("rjdesign.html"
                               ,html_project_detail=cfg_web_main
                               ,html_body=html_body
                               ,html_message_detail=myhtml.message_detail
                               ,html_menu_top=myhtml.html_menu_get(menu_type="topmenu",menu_list=cfg_web_pages)
                               ,html_menu_button=myhtml.html_menu_get(menu_type="buttonmenu",menu_list=cfg_web_pages)
                              )

    @app.route("/add_product", methods=["GET", 'POST'])
    def add_product():
        cfg_web_main["project_page_name"] = myhtml.page_name_get(page_url=request.path, page_list=cfg_web_pages)
        myhtml.message_detail = myhtml.html_message_set()
        html_body = ""
        item_name = ""
        item_desc = ""
        item_price = 0
        if request.method == "GET":
            html_body = form_add_item.replace("<<name_value>>",item_name).replace("<<description_value>>",item_desc).replace("<<price_value>>",str(item_price))
        else:
            item_name = request.form.get("name")
            item_desc = request.form.get("description")
            item_price = float(request.form.get("price"))
            if not item_name or not item_desc or not item_price or item_price<=0:
                myhtml.message_detail = myhtml.html_message_set(f"Invalid data!", "error")
                html_body = form_add_item.replace("<<name_value>>", item_name).replace("<<description_value>>",
                                                                                       item_desc).replace(
                    "<<price_value>>", str(item_price))
            else:
                sqlcommand = f"insert into items (name, description, price) values ('{item_name}', '{item_desc}', {item_price})"

                if examdb.sqlcommand_execute(sqlcommand):
                    myhtml.message_detail = myhtml.html_message_set(f"Product {item_name} added!")
                else:
                    myhtml.message_detail = myhtml.html_message_set(f"Error during data entry!","error")
                    html_body = form_add_item.replace("<<name_value>>",item_name).replace("<<description_value>>",item_desc).replace("<<price_value>>",str(item_price))

        return render_template("rjdesign.html"
                               , html_project_detail=cfg_web_main
                               , html_body=html_body
                               , html_message_detail=myhtml.message_detail
                               , html_menu_top=myhtml.html_menu_get(menu_type="topmenu", menu_list=cfg_web_pages)
                               , html_menu_button=myhtml.html_menu_get(menu_type="buttonmenu", menu_list=cfg_web_pages)
                               )

    @app.route("/databaseinfo", methods=["GET", 'POST'])
    def dbs_info():
        cfg_web_main["project_page_name"]=myhtml.page_name_get(page_url=request.path, page_list=cfg_web_pages)
        myhtml.message_detail = myhtml.html_message_set()
        html_body = ""
        sysinfo=examdb.sys_database_info()
        html_body += myhtml.table_detail_genertor(sysinfo)
        return render_template("rjdesign.html"
                               ,html_project_detail=cfg_web_main
                               ,html_body=html_body
                               ,html_message_detail=myhtml.message_detail
                               ,html_menu_top=myhtml.html_menu_get(menu_type="topmenu",menu_list=cfg_web_pages)
                               ,html_menu_button=myhtml.html_menu_get(menu_type="buttonmenu",menu_list=cfg_web_pages)
                              )
    if __name__ == "__main__":
        app.run(debug=True, port=5000)

    print("koncim...")
    examdb.close()

except Exception as err:
    print(f"{68*"_"}\nERROR\n {err}\n{68*"_"}")