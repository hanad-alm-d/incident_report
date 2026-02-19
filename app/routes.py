from flask import Blueprint, request, render_template
import os
from flask import current_app
import time
from werkzeug.utils import secure_filename

from .utils.docx_utils import fill_template_with_image
from .utils.email_utils import (
    send_email_with_attachment,
    start_email_server,
)

main = Blueprint("main", __name__)

FORMS_FOLDER = "forms"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        start_time = time.time()

        text_data = {
            "name": request.form.get("name", ""),
            "license": request.form.get("license", ""),
            "date": request.form.get("date", ""),
            "incident_time": request.form.get("incident_time", ""),
            "reported_time": request.form.get("reported_time", ""),
            "reported_by": request.form.get("reported_by", ""),
            "specific_area": request.form.get("specific_area", ""),
            "description": request.form.get("description", ""),
            "actions_taken": request.form.get("actions_taken", ""),
            "crime_related_incidents": request.form.get("crime_related_incidents", ""),
            "non_crime_related_incidents": request.form.get("non_crime_related_incidents", ""),
            "repored_to": "Security",
            "emergency_services_called": request.form.get("emergency_services_called", ""),
            "time_called": request.form.get("time_called", ""),
            "time_arrived": request.form.get("time_arrived", ""),
            "station_or_unit": request.form.get("station_or_unit", ""),
            "attending_officers": request.form.get("attending_officers", ""),
            "person1_type": request.form.get("person1_type", ""),
            "person1_full_name": request.form.get("person1_full_name", ""),
            "person1_dob": request.form.get("person1_dob", ""),
            "person1_age": request.form.get("person1_age", ""),
            "person1_postcode": request.form.get("person1_postcode", ""),
            "person1_address": request.form.get("person1_address", ""),
            "person1_suburb": request.form.get("person1_suburb", ""),
            "person1_phone1": request.form.get("person1_phone1", ""),
            "person1_phone2": request.form.get("person1_phone2", ""),
            "person2_type": request.form.get("person2_type", ""),
            "person2_full_name": request.form.get("person2_full_name", ""),
            "person2_dob": request.form.get("person2_dob", ""),
            "person2_age": request.form.get("person2_age", ""),
            "person2_postcode": request.form.get("person2_postcode", ""),
            "person2_address": request.form.get("person2_address", ""),
            "person2_suburb": request.form.get("person2_suburb", ""),
            "person2_phone1": request.form.get("person2_phone1", ""),
            "person2_phone2": request.form.get("person2_phone2", ""),
        }

        image_data = {}
        photo_path = None

        base_dir = current_app.root_path  # points to 'app/'
        forms_folder = os.path.join(base_dir, "forms")
        template_path = os.path.join(forms_folder, "incident_form_template.docx")
        output_path = os.path.join(forms_folder, "incident_form_filled.docx")

        photo = request.files.get("photo")

        if photo and allowed_file(photo.filename):
            filename = secure_filename(photo.filename)
            upload_folder = current_app.config["UPLOAD_FOLDER"]
            photo_path = os.path.join(upload_folder, filename)
            photo.save(photo_path)
            image_data["photo"] = (photo_path, 3.0, 3.0)

        fill_template_with_image(template_path, output_path, text_data, image_data)

        send_email_with_attachment(
            subject="Incident Report",
            body="Attached is the generated incident report.",
            to="hanadalimohamed1@gmail.com",
            attachment_path=output_path,
        )

        if photo_path and os.path.exists(photo_path):
            os.remove(photo_path)

        elapsed_time = time.time() - start_time
        return f"✅ Report submitted and emailed successfully in {elapsed_time:.2f} seconds!"

    return render_template("form.html")
