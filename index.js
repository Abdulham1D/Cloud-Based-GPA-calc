const express = require('express');
const { ApolloServer, gql } = require('apollo-server-express');
const { MongoClient, ServerApiVersion } = require('mongodb');

const uri = "mongodb+srv://moode:5CBMDAqKq148XR4Z@cluster0.brnf7ae.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

const typeDefs = gql`
  type Course {
    grade: String
    course: String
    hours: Int
  }

  type Query {
    courses: [Course]
  }
`;

const resolvers = {
  Query: {
    courses: async () => {
      await client.connect();
      const database = client.db("school");
      const coursesCollection = database.collection("courses");
      const courses = await coursesCollection.find().toArray();
      await client.close();
      return courses;
    }
  }
};

async function startApolloServer() {
  const app = express();
  const server = new ApolloServer({ typeDefs, resolvers });

  await server.start();
  server.applyMiddleware({ app, path: '/graphql' });

  const PORT = process.env.PORT || 8080;
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}${server.graphqlPath}`);
  });
}

startApolloServer().catch(err => {
  console.error('Error starting Apollo Server:', err);
});
