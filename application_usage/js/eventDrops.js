! function t(e, n, r) {
	function a(i, l) {
		if (!n[i]) {
			if (!e[i]) {
				var c = "function" == typeof require && require;
				if (!l && c) return c(i, !0);
				if (o) return o(i, !0);
				var s = new Error("Cannot find module '" + i + "'");
				throw s.code = "MODULE_NOT_FOUND", s
			}
			var u = n[i] = {
				exports: {}
			};
			e[i][0].call(u.exports, function(t) {
				var n = e[i][1][t];
				return a(n ? n : t)
			}, u, u.exports, t, e, n, r)
		}
		return n[i].exports
	}
	for (var o = "function" == typeof require && require, i = 0; i < r.length; i++) a(r[i]);
	return a
}({
	1: [function(t, e) {
		"use strict";
		var n = t("./eventDrops");
		"function" == typeof define && define.amd ? define("d3.chart.eventDrops", ["d3"], function(t) {
			t.chart = t.chart || {}, t.chart.eventDrops = n(t)
		}) : window ? (window.d3.chart = window.d3.chart || {}, window.d3.chart.eventDrops = n(window.d3)) : e.exports = n
	}, {
		"./eventDrops": 3
	}],
	2: [function(t, e) {
		"use strict";
		var n = t("./util/configurable"),
			r = {
				xScale: null,
				dateFormat: null
			};
		e.exports = function(t) {
			function e(e) {
				e.each(function() {
					d3.select(this).selectAll("text").remove();
					var e = t.xScale.domain();
					d3.select(this).append("text").text(function() {
						return t.dateFormat(e[0])
					}).classed("start", !0), d3.select(this).append("text").text(function() {
						return t.dateFormat(e[1])
					}).attr("text-anchor", "end").attr("transform", "translate(" + t.xScale.range()[1] + ")").classed("end", !0)
				})
			}
			t = t || {};
			for (var a in r) t[a] = t[a] || r[a];
			return n(e, t), e
		}
	}, {
		"./util/configurable": 6
	}],
	3: [function(t, e) {
		"use strict";
		var n = t("./util/configurable"),
			r = t("./eventLine"),
			a = t("./delimiter");
		e.exports = function(t) {
			var e = {
				start: new Date(0),
				end: new Date,
				minScale: 0,
				maxScale: 1 / 0,
				width: 1e3,
				margin: {
					top: 60,
					left: 200,
					bottom: 40,
					right: 50
				},
				locale: null,
				axisFormat: null,
				tickFormat: [
					[".%L", function(t) {
						return t.getMilliseconds()
					}],
					[":%S", function(t) {
						return t.getSeconds()
					}],
					["%I:%M", function(t) {
						return t.getMinutes()
					}],
					["%I %p", function(t) {
						return t.getHours()
					}],
					["%a %d", function(t) {
						return t.getDay() && 1 != t.getDate()
					}],
					["%b %d", function(t) {
						return 1 != t.getDate()
					}],
					["%B", function(t) {
						return t.getMonth()
					}],
					["%Y", function() {
						return !0
					}]
				],
				eventHover: null,
				eventZoom: null,
				hasDelimiter: !0,
				hasTopAxis: !0,
				hasBottomAxis: function(t) {
					return t.length >= 10
				},
				eventLineColor: "black",
				eventColor: null
			};
			return function(o) {
				function i(e) {
					e.each(function(e) {
						function n() {
							"[object MouseEvent]" === t.event.sourceEvent.toString() && m.translate([t.event.translate[0], 0]), "[object WheelEvent]" === t.event.sourceEvent.toString() && m.scale(t.event.scale), f()
						}

						function i() {
							h.select(".delimiter").remove();
							h.append("g").classed("delimiter", !0).attr("width", d).attr("height", 10).attr("transform", "translate(" + o.margin.left + ", " + (o.margin.top - 45) + ")").call(a({
								xScale: l,
								dateFormat: o.locale ? o.locale.timeFormat("%d %B %Y") : t.time.format("%d %B %Y")
							}))
						}

						function s() {
							o.eventZoom && o.eventZoom(l), o.hasDelimiter && i()
						}

						function u(e) {
							var n = [];
							o.tickFormat.forEach(function(t) {
								var e = t.slice(0);
								n.push(e)
							});
							var r = o.locale ? o.locale.timeFormat.multi(n) : t.time.format.multi(n),
								a = t.svg.axis().scale(l).orient(e).tickFormat(r);
							"function" == typeof o.axisFormat && o.axisFormat(a);
							var i = ("bottom" == e ? parseInt(v) : 0) + o.margin.top - 40;
							g.select(".x-axis." + e).remove();
							g.append("g").classed("x-axis", !0).classed(e, !0).attr("transform", "translate(" + o.margin.left + ", " + i + ")").call(a)
						}

						function f() {
							var t = "function" == typeof o.hasTopAxis ? o.hasTopAxis(e) : o.hasTopAxis;
							t && u("top");
							var n = "function" == typeof o.hasBottomAxis ? o.hasBottomAxis(e) : o.hasBottomAxis;
							n && u("bottom"), m.size([o.width, p]), g.select(".graph-body").remove();
							var a = g.append("g").classed("graph-body", !0).attr("transform", "translate(" + o.margin.left + ", " + (o.margin.top - 15) + ")"),
								i = a.selectAll("g").data(e);
							i.enter().append("g").classed("line", !0).attr("transform", function(t) {
								return "translate(0," + c(t.name) + ")"
							}).style("fill", o.eventLineColor).call(r({
								xScale: l,
								eventColor: o.eventColor
							})), i.exit().remove()
						}
						var m = t.behavior.zoom().center(null).scaleExtent([o.minScale, o.maxScale]).on("zoom", n);
						m.on("zoomend", s);
						var d = o.width - o.margin.right - o.margin.left,
							v = 40 * e.length,
							p = v + o.margin.top + o.margin.bottom;
						t.select(this).select("svg").remove();
						var h = t.select(this).append("svg").attr("width", o.width).attr("height", p),
							g = h.append("g").attr("transform", "translate(0, 25)"),
							x = [],
							w = [];
						e.forEach(function(t, e) {
							x.push(t.name), w.push(40 * e)
						}), c.domain(x).range(w);
						var b = g.append("g").classed("y-axis", !0).attr("transform", "translate(0, 60)"),
							y = b.append("g").selectAll("g").data(x);
						y.enter().append("g").attr("transform", function(t) {
							return "translate(0, " + c(t) + ")"
						}).append("line").classed("y-tick", !0).attr("x1", o.margin.left).attr("x2", o.margin.left + d), y.exit().remove();
						var S, D, A = h.append("rect").call(m).classed("zoom", !0).attr("width", d).attr("height", p).attr("transform", "translate(" + o.margin.left + ", 35)");
						"function" == typeof o.eventHover && A.on("mousemove", function() {
							var e = t.event;
							if (S != e.clientX || D != e.clientY) {
								S = e.clientX, D = e.clientY, A.attr("display", "none");
								var n = document.elementFromPoint(t.event.clientX, t.event.clientY);
								A.attr("display", "block"), "circle" === n.tagName && o.eventHover(n)
							}
						}), l.range([0, d]).domain([o.start, o.end]), m.x(l), f(), o.hasDelimiter && i(), o.eventZoom && o.eventZoom(l)
					})
				}
				var l = t.time.scale(),
					c = t.scale.ordinal();
				o = o || {};
				for (var s in e) o[s] = o[s] || e[s];
				return n(i, o), i
			}
		}
	}, {
		"./delimiter": 2,
		"./eventLine": 4,
		"./util/configurable": 6
	}],
	4: [function(t, e) {
		"use strict";
		var n = t("./util/configurable"),
			r = t("./filterData"),
			a = {
				xScale: null
			};
		e.exports = function(t) {
			t = t || {
				xScale: null,
				eventColor: null
			};
			for (var e in a) t[e] = t[e] || a[e];
			var o = function(e) {
				e.each(function() {
					d3.select(this).selectAll("text").remove(), d3.select(this).append("text").text(function(e) {
						var n = r(e.dates, t.xScale).length;
						return e.name + (n > 0 ? " (" + n + ")" : "")
					}).attr("text-anchor", "end").attr("transform", "translate(-20)").style("fill", "black"), d3.select(this).selectAll("circle").remove();
					var e = d3.select(this).selectAll("circle").data(function(e) {
						return r(e.dates, t.xScale)
					});
					e.enter().append("circle").attr("cx", function(e) {
						return t.xScale(e)
					}).style("fill", t.eventColor).attr("cy", -5).attr("r", 10), e.exit().remove()
				})
			};
			return n(o, t), o
		}
	}, {
		"./filterData": 5,
		"./util/configurable": 6
	}],
	5: [function(t, e) {
		"use strict";
		e.exports = function(t, e) {
			t = t || [];
			var n = [],
				r = e.range(),
				a = r[0],
				o = r[1];
			return t.forEach(function(t) {
				var r = e(t);
				a > r || r > o || n.push(t)
			}), n
		}
	}, {}],
	6: [function(t, e) {
		e.exports = function(t, e, n) {
			n = n || {};
			for (var r in e) ! function(r) {
				t[r] = function(a) {
					return arguments.length ? (e[r] = a, n.hasOwnProperty(r) && n[r](a), t) : e[r]
				}
			}(r)
		}
	}, {}]
}, {}, [1]);