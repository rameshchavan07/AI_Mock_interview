/** @type { import("drizzle-kit").Config } */
export default {
  schema: "./utils/schema.js",
  dialect: "postgresql",
  dbCredentials: {
    url: "postgresql://ai-interview-mocker_owner:Ney4wumsSz7k@ep-orange-bread-a5xau0xo.us-east-2.aws.neon.tech/ai-interview-mocker?sslmode=require",
  },
};
