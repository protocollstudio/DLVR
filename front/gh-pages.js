var ghpages = require('gh-pages.cjs');

ghpages.publish(
    'public', // path to public directory
    {
        branch: 'gh-pages',
        repo: 'https://github.com/protocollstudio/DLVR', // Update to point to your repository  
        user: {
            name: 'pipazoul', // update to use your name
            email: 'yassin@siouda.com' // Update to use your email
        }
    },
    () => {
        console.log('Deploy Complete!')
    }
)