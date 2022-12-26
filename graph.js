Promise.all([
  fetch('graphs/notes.json', {mode: 'no-cors'})
    .then(function(res) {
      return res.json()
    })
])
  .then(function(dataArray) {
    var cy = cytoscape({
      container: document.getElementById('cy'),
      elements: dataArray[0]['elements'],
      style: [ // the stylesheet for the graph
        {
          selector: 'node',
          style: {
            'width': ele => ele.outdegree() * 2 + ele.indegree() * 5,
            'height': ele => ele.outdegree() * 2 + ele.indegree() * 5,
            'background-color': 'data(color)',
            'label': 'data(id)',
            'font-size': '10px',
            'text-border-width': '2px',
            'text-border-color': 'black',
            'text-border-opacity': '1',
            'text-background-color': 'black',
            'text-background-opacity': '0.4',
            'color': 'white',
            'shape': 'data(shape)',
            'border-style': 'solid',
            'border-color': 'data(border)',
            'border-opacity': '1',
            'border-width': '3px',
            'text-valign': 'center',
            'text-halign': 'center',
            'text-wrap': 'ellipsis',
            'text-max-width': ele => ele.outdegree() * 2 + ele.indegree() * 5,
          }
        },

        {
          selector: 'edge',
          style: {
            'width': '2',
            'line-color': 'mapData(weight, 0, 5, gray, white)',
            'target-arrow-color': 'mapData(weight, 0, 5, gray, white)',
            'target-arrow-shape': 'triangle',
            'curve-style': 'bezier'
          }
        }
      ],
      layout: {
        name: 'cose',
      
        // Called on `layoutready`
        ready: function(){},
      
        // Called on `layoutstop`
        stop: function(){},
      
        // Whether to animate while running the layout
        // true : Animate continuously as the layout is running
        // false : Just show the end result
        // 'end' : Animate with the end result, from the initial positions to the end positions
        animate: true,
      
        // Easing of the animation for animate:'end'
        animationEasing: 200,
      
        // The duration of the animation for animate:'end'
        animationDuration: 200,
      
        // A function that determines whether the node should be animated
        // All nodes animated by default on animate enabled
        // Non-animated nodes are positioned immediately when the layout starts
        animateFilter: function ( node, i ){ return true; },
      
      
        // The layout animates only after this many milliseconds for animate:true
        // (prevents flashing on fast runs)
        animationThreshold: 250,
      
        // Number of iterations between consecutive screen positions update
        refresh: 50,
      
        // Whether to fit the network view after when done
        fit: false,
      
        // Padding on fit
        padding: 20,
      
        // Constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }
        boundingBox: undefined,
      
        // Excludes the label when calculating node bounding boxes for the layout algorithm
        nodeDimensionsIncludeLabels: false,
      
        // Randomize the initial positions of the nodes (true) or use existing positions (false)
        randomize: false,
      
        // Extra spacing between components in non-compound graphs
        componentSpacing: 40,
      
        // Node repulsion (non overlapping) multiplier
        nodeRepulsion: function( node ){ return 4098; },
      
        // Node repulsion (overlapping) multiplier
        nodeOverlap: 8,
      
        // Ideal edge (non nested) length
        idealEdgeLength: function( edge ){ return 32; },
      
        // Divisor to compute edge forces
        edgeElasticity: function( edge ){ return 32; },
      
        // Nesting factor (multiplier) to compute ideal edge length for nested edges
        nestingFactor: 1.2,
      
        // Gravity force (constant)
        gravity: 1,
      
        // Maximum number of iterations to perform
        numIter: 2000,
      
        // Initial temperature (maximum node displacement)
        initialTemp: 3000,
      
        // Cooling factor (how the temperature is reduced between consecutive iterations
        coolingFactor: 0.99,
      
        // Lower temperature threshold (below this point the layout will end)
        minTemp: 1.0
      }
    })
  })



