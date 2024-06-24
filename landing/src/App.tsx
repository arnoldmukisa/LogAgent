import { useState } from 'react';
import './App.css';
import './index.css';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, BarChart, Bar } from 'recharts';
import dashboardImage from './assets/dashboard.png';

const Header = () => (
  <header className="bg-gray-900 text-white py-4 sticky top-0 z-50">
    <div className="container mx-auto px-4 flex justify-between items-center">
      <h1 className="text-2xl font-bold">LogAgent</h1>
      <nav>
        <ul className="flex space-x-6">
          <li><a href="#about" className="hover:text-blue-400 transition duration-300">About</a></li>
          <li><a href="#features" className="hover:text-blue-400 transition duration-300">Features</a></li>
          <li><a href="#use-case" className="hover:text-blue-400 transition duration-300">Use Case</a></li>
          <li><a href="#demo" className="hover:text-blue-400 transition duration-300">Demo</a></li>
        </ul>
      </nav>
    </div>
  </header>
);

const Hero = () => (
  <section className="bg-gradient-to-r from-gray-900 to-blue-900 text-white py-20">
    <div className="container mx-auto px-4 flex flex-col md:flex-row items-center">
      <div className="md:w-1/2 mb-8 md:mb-0">
        <h2 className="text-4xl font-bold mb-4">LogAgent: AI-Powered Log Analysis</h2>
        <p className="text-xl mb-8">Efficiently debug production issues with advanced anomaly detection and root cause analysis</p>
        <a href="https://github.com/arnoldmukisa/LogAgent" className="bg-blue-600 text-white py-2 px-6 rounded-lg font-bold hover:bg-blue-700 transition duration-300">View on GitHub</a>
      </div>
      <div className="md:w-1/2">
        <img src={dashboardImage} alt="LogAgent Dashboard" className="rounded-lg shadow-2xl" />
      </div>
    </div>
  </section>
);

const About = () => (
  <section id="about" className="py-16 bg-gray-100">
    <div className="container mx-auto px-4">
      <h2 className="text-3xl font-bold mb-8 text-center">About LogAgent</h2>
      <div className="bg-white rounded-lg shadow-lg p-8">
        <p className="text-lg mb-4">
          LogAgent is an open-source tool that leverages Large Language Models (LLMs) to analyze log files, interpret event flows, and identify subtle anomalies that traditional error detection methods might miss.
        </p>
        <p className="text-lg">
          It's specifically designed to address complex logic and business flow issues in production environments, significantly reducing the time required for issue diagnosis and resolution.
        </p>
      </div>
    </div>
  </section>
);

interface FeatureCardProps {
  title: string;
  description: string;
  icon: string;
}

const FeatureCard = ({ title, description, icon }: FeatureCardProps) => (
  <div className="bg-white rounded-lg shadow-lg p-6 transition-all duration-300 hover:shadow-xl hover:scale-105">
    <div className="text-4xl text-blue-600 mb-4">{icon}</div>
    <h3 className="text-xl font-bold mb-2">{title}</h3>
    <p>{description}</p>
  </div>
);

const Features = () => (
  <section id="features" className="py-16 bg-gray-200">
    <div className="container mx-auto px-4">
      <h2 className="text-3xl font-bold mb-8 text-center">Key Features</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <FeatureCard 
          icon="🧠"
          title="LLM-Based Analysis" 
          description="Utilizes state-of-the-art language models for advanced pattern recognition in log data"
        />
        <FeatureCard 
          icon="🔍"
          title="Anomaly Detection" 
          description="Identifies logic issues and business flow anomalies that don't trigger traditional error alerts"
        />
        <FeatureCard 
          icon="📊"
          title="Large File Processing" 
          description="Efficiently handles log files up to 256k tokens, suitable for extensive production logs"
        />
        <FeatureCard 
          icon="🔬"
          title="Context-Aware Insights" 
          description="Provides detailed analysis considering the full context of the application's behavior"
        />
        <FeatureCard 
          icon="🔓"
          title="Open Source" 
          description="Fully customizable and extensible to fit specific organizational needs"
        />
        <FeatureCard 
          icon="🎯"
          title="Root Cause Analysis" 
          description="Accelerates issue resolution by pinpointing the underlying causes of production problems"
        />
      </div>
    </div>
  </section>
);

const UseCaseExample = () => {
  const [activeTab, setActiveTab] = useState('findings');
  
  const logLevelData = [
    { name: 'INFO', count: 97 },
    { name: 'DEBUG', count: 81 },
    { name: 'WARN', count: 11 },
    { name: 'ERROR', count: 3 },
  ];

  const errorRateData = [
    { time: '04 PM', rate: 33 },
    { time: '05 PM', rate: 7 },
    { time: '06 PM', rate: 6 },
    { time: '07 PM', rate: 17 },
    { time: '08 PM', rate: 7 },
    { time: '09 PM', rate: 9 },
    { time: '10 PM', rate: 8 },
    { time: '11 PM', rate: 6 },
    { time: '12 AM', rate: 7 },
    { time: '01 AM', rate: 22 },
    { time: '02 AM', rate: 8 },
    { time: '03 AM', rate: 3 },
  ];

  return (
    <section id="use-case" className="py-16 bg-white">
      <div className="container mx-auto px-4">
        <h2 className="text-3xl font-bold mb-8 text-center">Real-World Use Case Analysis</h2>
        <div className="bg-gray-100 rounded-lg shadow-lg p-8">
          <h3 className="text-2xl font-semibold mb-4">Scenario: AMER Region Order Fulfillment Issue</h3>
          <p className="mb-4 text-lg">
            Unfulfilled orders for PROD-X in the AMER region, potentially due to inventory or fulfillment issues.
          </p>
          
          <div className="mb-6">
            <div className="flex border-b">
              <button 
                className={`py-2 px-4 ${activeTab === 'findings' ? 'border-b-2 border-blue-500 text-blue-500' : 'text-gray-500'}`}
                onClick={() => setActiveTab('findings')}
              >
                Key Findings
              </button>
              <button 
                className={`py-2 px-4 ${activeTab === 'rootCause' ? 'border-b-2 border-blue-500 text-blue-500' : 'text-gray-500'}`}
                onClick={() => setActiveTab('rootCause')}
              >
                Root Cause
              </button>
              <button 
                className={`py-2 px-4 ${activeTab === 'actions' ? 'border-b-2 border-blue-500 text-blue-500' : 'text-gray-500'}`}
                onClick={() => setActiveTab('actions')}
              >
                Recommended Actions
              </button>
            </div>
            <div className="mt-4">
              {activeTab === 'findings' && (
                <ul className="list-disc list-inside space-y-2">
                  <li>Successful order fulfillment for ORD-APAC-001 and ORD-EMEA-001</li>
                  <li>ORD-AMER-001 placed for 300 units of PROD-X in AMER region</li>
                  <li>Inventory discrepancy detected: expected 300 units, actual 370 units of PROD-X</li>
                </ul>
              )}
              {activeTab === 'rootCause' && (
                <ul className="list-disc list-inside space-y-2">
                  <li>Daily inventory allocation job (23:55 UTC) creates a race condition</li>
                  <li>Timezone mismatch in inventory allocation process</li>
                  <li>Regional inventory check occurs before correct allocation, leading to overselling</li>
                </ul>
              )}
              {activeTab === 'actions' && (
                <ul className="list-disc list-inside space-y-2">
                  <li>Implement timezone-aware inventory allocation process</li>
                  <li>Introduce distributed locking for inventory allocation and order reservation</li>
                  <li>Develop a caching mechanism for regional inventory with proper invalidation</li>
                  <li>Implement automatic retry logic for failed orders with exponential backoff</li>
                  <li>Create separate regional inventory reports post-allocation for auditing</li>
                </ul>
              )}
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-6">
            <div>
              <h4 className="text-xl font-semibold mb-4">Log Level Distribution</h4>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={logLevelData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="count" fill="#3b82f6" />
                </BarChart>
              </ResponsiveContainer>
            </div>
            <div>
              <h4 className="text-xl font-semibold mb-4">Error Rate Over Time</h4>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={errorRateData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="time" />
                  <YAxis />
                  <Tooltip />
                  <Line type="monotone" dataKey="rate" stroke="#3b82f6" strokeWidth={2} />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

const Demo = () => {
  const codeExample = `
import logagent

# Initialize LogAgent
agent = logagent.LogAgent()

# Load and analyze log file
analysis = agent.analyze("path/to/logfile.log")

# Get key insights
insights = analysis.get_insights()

# Print root cause
print("Root Cause:", analysis.get_root_cause())

# Get recommended actions
actions = analysis.get_recommended_actions()

# Visualize log level distribution
analysis.plot_log_level_distribution()
  `;

  return (
    <section id="demo" className="py-16 bg-gray-100">
      <div className="container mx-auto px-4">
        <h2 className="text-3xl font-bold mb-8 text-center">LogAgent in Action</h2>
        <div className="bg-white rounded-lg shadow-lg p-8">
          <h3 className="text-2xl font-semibold mb-4">Sample Usage</h3>
          <pre className="bg-gray-900 text-green-400 p-4 rounded-lg overflow-x-auto">
            <code>{codeExample}</code>
          </pre>
        </div>
      </div>
    </section>
  );
};

const Footer = () => (
  <footer className="bg-gray-900 text-white py-8">
    <div className="container mx-auto px-4 text-center">
      <p>&copy; 2024 LogAgent. All rights reserved.</p>
      <div className="mt-4">
        <a href="https://github.com/arnoldmukisa/LogAgent" className="text-blue-400 hover:text-blue-300 mx-2 transition duration-300">GitHub</a>
        <a href="#" className="text-blue-400 hover:text-blue-300 mx-2 transition duration-300">Documentation</a>
        <a href="#" className="text-blue-400 hover:text-blue-300 mx-2 transition duration-300">API Reference</a>
      </div>
    </div>
  </footer>
);

const App = () => {
  return (
    <div className="font-sans bg-white text-gray-900">
      <Header />
      <Hero />
      <About />
      <Features />
      <UseCaseExample />
      <Demo />
      <Footer />
    </div>
  );
};

export default App;
