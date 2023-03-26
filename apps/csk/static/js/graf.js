window.onload = function() {
            
    var chart = new CanvasJS.Chart("chartContainer", {       
        animationEnabled: true,
        title: {
            text: "Собранные деньги за 2022 г"
        },
        // axisX:{
        //     minimum: 1,
        //     maximum: 12
        // },
        data: [{
            type: "column",
            yValueFormatString: "#,##0.00 тг",
            dataPoints: [
                { label: "январь(Ремонт подъезда)", y: 57466.787 },
                { label: "февраль(Замена крыши)", y: 49927.82 },
                { label: "март(Ремонт подвала)", y: 39899.388 },
                { label: "апрель(Уборка мусора)", y: 37622.207 },
                { label: "май(Ремонт лифта)", y: 8649.948 },
                { label: "июнь(Капитальный ремонт дома)", y: 8123.181 },
                { label: "июль(Сбор денег)", y: 3570.295 },
                { label: "август(Сбор денег)", y: 1709.387 },
                { label: "сентябрь(Сбор денег)", y: 1709.387 },
                { label: "октябрь(Сбор денег)", y: 1709.387 },
                { label: "ноябрь(Сбор денег)", y: 1709.387 },
                { label: "декабрь(Сбор денег)", y: 1709.387 }
            ]
        }]
    });
    chart.render();
    
    var xSnapDistance = chart.axisX[0].convertPixelToValue(chart.get("dataPointWidth")) / 2;
    var ySnapDistance = 3;
    
    var xValue, yValue;
    
    var mouseDown = false;
    var selected = null;
    var changeCursor = false;
    
    var timerId = null;
    
    function getPosition(e) {
        var parentOffset = $("#chartContainer > .canvasjs-chart-container").offset();          	
        var relX = e.pageX - parentOffset.left;
        var relY = e.pageY - parentOffset.top;
        xValue = Math.round(chart.axisX[0].convertPixelToValue(relX));
        yValue = Math.round(chart.axisY[0].convertPixelToValue(relY));
    }
    
    function searchDataPoint() {
        var dps = chart.data[0].dataPoints;
        for(var i = 0; i < dps.length; i++ ) {
            if( (xValue >= dps[i].x - xSnapDistance && xValue <= dps[i].x + xSnapDistance) && (yValue >= dps[i].y - ySnapDistance && yValue <= dps[i].y + ySnapDistance) ) 
            {
                if(mouseDown) {
                    selected = i;
                    break;
                } else {
                    changeCursor = true;
                    break; 
                }
            } else {
                selected = null;
                changeCursor = false;
            }
        }
    }
    
    jQuery("#chartContainer > .canvasjs-chart-container").on({
        mousedown: function(e) {
            mouseDown = true;
            getPosition(e);  
            searchDataPoint();
        },
        mousemove: function(e) {
            getPosition(e);
            if(mouseDown) {
                clearTimeout(timerId);
                timerId = setTimeout(function(){
                    if(selected != null) {
                        chart.data[0].dataPoints[selected].y = yValue;
                        chart.render();
                    }   
                }, 0);
            }
            else {
                searchDataPoint();
                if(changeCursor) {
                    chart.data[0].set("cursor", "n-resize");
                } else {
                    chart.data[0].set("cursor", "default");
                }
            }
        },
        mouseup: function(e) {
            if(selected != null) {
                chart.data[0].dataPoints[selected].y = yValue;
                chart.render();
                mouseDown = false;
            }
        }
    });
    
    }



    
