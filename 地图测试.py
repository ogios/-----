import folium, geopandas as gpd
from branca.colormap import LinearColormap as lcm
china=folium.Map(location=[35,107.4],zoom_start=4,max_zoom=5,min_zoom=3,control_scale=True,tiles='cartodb positron')

pros=gpd.read_file(r'C:\Users\MOIiii\Desktop\中国省份地图文件\中国省级地图GS（2019）1719号.geojson')
nor=gpd.read_file(r'C:\Users\MOIiii\Desktop\中国省份地图文件\九段线GS（2019）1719号.geojson')
pros['薪资']=[i*1000 for i in range(len(pros.iloc[:,0]))]

df=pros.iloc[:,0:1]
df['value']=[i*1000 for i in range(len(pros.iloc[:,0]))]
df.index=df['CNAME']
df=df.iloc[:,1]


colormap=lcm(['#47accf','#fd883a','#c00225']).scale(df.min(),df.max())


gjson=folium.GeoJson(
    pros,
    name='薪资',
    style_function=lambda feature: {
        "fillColor": colormap(df[feature["properties"]['CNAME']]),
        "color": "black",
        "weight": 0,
        "fillOpacity": 0.8,
    },
)
gjson.add_to(china)
folium.features.GeoJsonTooltip(fields=['CNAME','薪资']).add_to(gjson)

folium.TileLayer('openstreetmap').add_to(china)
# folium.TileLayer('mapquestopen').add_to(china)
# folium.TileLayer('MapQuest Open Aerial').add_to(china)
# folium.TileLayer('Mapbox Bright').add_to(china)
# folium.TileLayer('Mapbox Control Room').add_to(china)
folium.TileLayer('stamenterrain').add_to(china)
folium.TileLayer('cartodbpositron').add_to(china)
folium.TileLayer('stamentoner').add_to(china)
folium.TileLayer('cartodbdark_matter').add_to(china)
folium.TileLayer('cartodb positron').add_to(china)
folium.TileLayer('stamenwatercolor').add_to(china)
folium.LayerControl().add_to(china)


china.save('foliun.html')
