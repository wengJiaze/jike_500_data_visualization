from unittest.mock import patch

from nose.tools import assert_in, eq_

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_geo_base(fake_writer):
    c = (
        Geo()
        .add_schema(maptype="china")
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
    )
    eq_(c.theme, "white")
    c.render()
    _, content = fake_writer.call_args[0]
    assert_in("canvas", content)


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_extra_geo_parameters(fake_writer):
    c = (
        Geo()
        .add_schema(maptype="china", center=[39, 117.7], zoom=9)
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
    )
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
    c.render()
    _, content = fake_writer.call_args[0]
    center_string = """
        "center": [
            39,
            117.7
        ],
    """
    assert_in(center_string, content)
    assert_in('"zoom": 9', content)


def test_geo_dump_options():
    c = (
        Geo()
        .add_schema(maptype="china", center=[39, 117.7], zoom=9)
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .set_global_opts(visualmap_opts=opts.VisualMapOpts())
    )
    formatter = """"formatter": function (params) {        return params.name + ' : ' + params.value[2];    }"""  # noqa
    assert_in(formatter, c.dump_options())
