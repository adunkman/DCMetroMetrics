'use strict';

/**
 * @ngdoc directive
 * @name dcmetrometricsApp.directive:unitHeatmap
 * @description
 * # unitHeatmap
 */
angular.module('dcmetrometricsApp')
  .directive('unitCalendarHeatmap', function () {
    return {
      templateUrl: '/views/unit_calendar_heatmap_partial.html',
      restrict: 'E',
      replace: true,
      scope: {
        type : '@',
        unitid : '@',
        data : '=',
        legend: '@',
        legendColors: '@',
        legendMinColor: '@',
        legendMaxColor: '@',
        header: '@',
        description: '@',
        tooltip: '@',
        displayLegend: '@',
        considerMissingDataAsZero: '@'
      }, 

      controller: ['$scope', function($scope) {

        $scope.id_pfx = 'dcmm-unit-cal-heatmap-' + $scope.type + '-' + $scope.unitid;
 
      }],

      link: function postLink(scope, element, attrs) {


        // console.log('unit calendar heatmap!', scope.id_pfx);
        // console.log(element);

        var children = element.children();

        var cal;

      
        // Look for data changes, and redraw the calendar
        scope.$watch('data', function(data) {
          

          if (!data) { return; }

          var tooltip = eval(scope.tooltip);
          var legend = eval(scope.legend);
          var legendColors = scope.$eval(scope.legendColors);
          var displayLegend = eval(scope.displayLegend);
          var considerMissingDataAsZero = eval(scope.considerMissingDataAsZero) || false;

          // console.log(scope);


          if(cal) { cal = cal.destroy(); }

          cal = new CalHeatMap();

          var months_to_display = 4;
          cal.init({
            itemSelector: element.find('#' + scope.id_pfx + '-cal')[0],
            previousSelector:element.find('#' + scope.id_pfx + '-previous')[0],
            nextSelector: element.find('#' + scope.id_pfx + '-next')[0],
            data: data,
            domain: "month",
            range: months_to_display,
            subDomain: "x_day",
            start: moment().subtract(months_to_display-1, 'months').toDate(),
            cellSize: 20,
            cellPadding: 5,
            domainGutter: 20,
            domainLabelFormat: function(date) {
              moment.lang("en");
              return moment(date).format("MMMM YYYY").toUpperCase();
            },
            subDomainTextFormat: "%d",
            domainDynamicDimension: false,
            legend: legend,
            legendColors: legendColors,
            displayLegend: displayLegend,
            minDate : new Date(2013, 5, 1),
            maxDate : new Date(),
            tooltip: tooltip,
            weekStartOnMonday: false,
            considerMissingDataAsZero: considerMissingDataAsZero
          });

        });

      }

    };
  });
