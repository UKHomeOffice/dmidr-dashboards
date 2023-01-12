# Deployment Process

## Pushing a new version of the Docker image

1. Create a pull request with your changes.
1. Add a label to the pull request, one of major, minor or patch, depending on your changes.
The label will determine how the version number is incremented, following `major.minor.patch`.
The pipeline will fail without this label and a new image will not be pushed to the repository.
1. After the tests have passed, merge the pull request.
1. A [Github actions workflow][push_image_workflow] will rerun the tests.
If they pass, it will build the docker image.
It will then push the image to the [quay repository][quay_repository], tagged with the new version number and create a matching tag in the github repository.
1. The creation of a tag in the github repository will trigger the [drone pipeline][drone_pipeline] to run and deploy the image to the kubernetes cluster.


# Local Develpoment
## Deploying the app

1. Local development with seed data requires the [Transformation](https://github.com/UKHomeOffice/hocs-mi-transformation) Database to be deployed.

2. This also requires the [Transformation](https://github.com/UKHomeOffice/hocs-mi-transformation) process to be completed.

3. Setup the virtual environment
```
$ make build
$ make serve-transformation
$ make serve
```

4. Clean down the [Transformation](https://github.com/UKHomeOffice/hocs-mi-transformation) repository
```
$ make stop
$ make clean
```


[quay_repository]: https://quay.io/repository/ukhomeofficedigital/hocs-mi-dashboards?tab=tags&tag=latest
[push_image_workflow]: https://github.com/UKHomeOffice/hocs-mi-dashboards/actions/workflows/docker-push.yml
[drone_pipeline]: https://drone-gh.acp.homeoffice.gov.uk/UKHomeOffice/hocs-mi-dashboards

# Command to run locally
```
$ PYTHONPATH=./ python app/index.py
```

# Creating a new report.
1. Create query within `app\data\{user group}\ `, with any mock data needed to enable local development.
2. Create the report page within `app\pages\ `.
   1. Within the new page, register the report as a new page with dash.
    ```python
    import dash
    
    dash.register_page(
        __name__, 
        name="Example Report",
        path="/example-report"
    )
    ```
   2. A report base has been created which set out the general formatting of the page. Usage of this can be seen below. <br> Visualisations should be added as part of the body as an array of Dash [html](https://dash.plotly.com/dash-html-components) and [dcc](https://dash.plotly.com/dash-core-components) components. Some generic visualisations have been created and can be found within `app\components\ `
    ```python
    from app.pages.report_base import report_base
    
    layout = report_base(title="Example report", body=[...]
    ```
   3. Add report navigation card to [home page](app/pages/home.py).
   ```python
   html.Div(
        className="decs-grid-row",
        style={"paddingTop":"15px"},
        children=[
            board_link_card(dash_title="Performance summary", dash_link="/performance-summary"),
            board_link_card(dash_title="Intake and output", dash_link="/intake-output"),
            board_link_card(dash_title="Example report", dash_link="/example-report"),
        ]
   )
   ```
   4. Add interactivity such as filtering through the use of [callbacks](https://dash.plotly.com/basic-callbacks).