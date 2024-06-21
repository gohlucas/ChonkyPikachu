module.exports = {
    async redirects() {
      return [
        {
          source: '/',
          destination: '/intro', // Adjust this path according to your new directory structure
          permanent: true,
        },
      ];
    },
  };