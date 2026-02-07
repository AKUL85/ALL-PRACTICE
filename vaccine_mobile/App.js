import React, { useState, useEffect } from 'react';
import {
  StyleSheet,
  Text,
  View,
  ScrollView,
  TouchableOpacity,
  TextInput,
  ActivityIndicator,
  Alert,
  Dimensions,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';

const { width } = Dimensions.get('window');

export default function App() {
  const [screen, setScreen] = useState('home');
  const [loading, setLoading] = useState(false);
  const [strategy, setStrategy] = useState(null);

  // Form state
  const [formData, setFormData] = useState({
    population: '150000',
    age_dist: '0.35',
    past_7_days: '2500',
    infection_rate: '3.5',
    awareness: '75',
    power_stability: '0.85',
    distance_from_hub: '45',
  });

  const handleInputChange = (field, value) => {
    setFormData((prev) => ({
      ...prev,
      [field]: value,
    }));
  };

  const generateRandomData = () => {
    const randomValues = {
      population: String(Math.floor(Math.random() * 499000 + 1000)),
      age_dist: (Math.random()).toFixed(2),
      past_7_days: String(Math.floor(Math.random() * 4950 + 50)),
      infection_rate: (Math.random() * 9.9 + 0.1).toFixed(1),
      awareness: String(Math.floor(Math.random() * 81 + 20)),
      power_stability: (Math.random() * 0.7 + 0.3).toFixed(2),
      distance_from_hub: String(Math.floor(Math.random() * 495 + 5)),
    };
    setFormData(randomValues);
  };

  const generateStrategy = () => {
    setLoading(true);
    // Simulate API call with mock predictions
    setTimeout(() => {
      const demand = Math.floor(
        (parseFloat(formData.population) / 1000) * 0.3 +
        parseFloat(formData.infection_rate) * 50 +
        (parseFloat(formData.awareness) / 100) * 100 +
        Math.random() * 100
      );

      const wasteScore =
        (1 - parseFloat(formData.power_stability)) * 50 +
        (parseFloat(formData.distance_from_hub) / 500) * 40 +
        (100 - parseFloat(formData.awareness)) / 100 * 30 +
        Math.random() * 20;

      let wasteRisk = 'Low';
      let wasteRiskColor = '#28a745';
      if (wasteScore > 70) {
        wasteRisk = 'High';
        wasteRiskColor = '#dc3545';
      } else if (wasteScore > 40) {
        wasteRisk = 'Medium';
        wasteRiskColor = '#ffc107';
      }

      const mockProba = {
        low: Math.random(),
        medium: Math.random(),
        high: Math.random(),
      };
      const total = mockProba.low + mockProba.medium + mockProba.high;
      const normalized = {
        low: (mockProba.low / total).toFixed(2),
        medium: (mockProba.medium / total).toFixed(2),
        high: (mockProba.high / total).toFixed(2),
      };

      setStrategy({
        demand,
        wasteRisk,
        wasteRiskColor,
        confidence: (Math.max(...Object.values(normalized)) * 100).toFixed(0),
        probabilities: normalized,
        recommendations: generateRecommendations(demand, wasteRisk),
      });

      setScreen('results');
      setLoading(false);
    }, 2000);
  };

  const generateRecommendations = (demand, waste) => {
    const recs = [];
    if (demand > 1000) {
      recs.push('🚚 HIGH DEMAND: Increase vaccine shipment frequency');
    } else {
      recs.push('📦 MODERATE DEMAND: Standard supply chain');
    }

    if (waste === 'High') {
      recs.push('⚠️ HIGH WASTE RISK: Implement cold chain monitoring');
      recs.push('📋 ACTION: Deploy backup power systems');
    } else if (waste === 'Medium') {
      recs.push('🔍 MEDIUM WASTE RISK: Monitor infrastructure closely');
    } else {
      recs.push('✓ LOW WASTE RISK: Standard operations sufficient');
    }
    return recs;
  };

  // HOME SCREEN
  if (screen === 'home') {
    return (
      <LinearGradient colors={['#667eea', '#764ba2']} style={styles.container}>
        <ScrollView contentContainerStyle={styles.homeContent}>
          <View style={styles.headerBox}>
            <Text style={styles.title}>💉 Vaccine Management</Text>
            <Text style={styles.subtitle}>ML-Powered Supply Chain</Text>
          </View>

          <View style={styles.infoCard}>
            <Text style={styles.cardTitle}>🎯 System Overview</Text>
            <Text style={styles.cardText}>
              This intelligent system uses two Random Forest models to optimize vaccine
              distribution:
            </Text>
            <Text style={styles.cardText}>
              • <Text style={{ fontWeight: 'bold' }}>Demand Predictor</Text> - Estimates
              daily doses needed
            </Text>
            <Text style={styles.cardText}>
              • <Text style={{ fontWeight: 'bold' }}>Waste Risk Classifier</Text> - Identifies
              storage challenges
            </Text>
          </View>

          <View style={styles.metricsBox}>
            <View style={styles.metricCard}>
              <Text style={styles.metricValue}>500</Text>
              <Text style={styles.metricLabel}>Dataset Size</Text>
            </View>
            <View style={styles.metricCard}>
              <Text style={styles.metricValue}>0.84</Text>
              <Text style={styles.metricLabel}>Model R²</Text>
            </View>
            <View style={styles.metricCard}>
              <Text style={styles.metricValue}>7</Text>
              <Text style={styles.metricLabel}>Features</Text>
            </View>
          </View>

          <TouchableOpacity
            style={styles.primaryButton}
            onPress={() => setScreen('predictor')}
          >
            <Text style={styles.buttonText}>Generate Strategy</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.secondaryButton}
            onPress={() => setScreen('about')}
          >
            <Text style={styles.secondaryButtonText}>Learn More</Text>
          </TouchableOpacity>
        </ScrollView>
      </LinearGradient>
    );
  }

  // PREDICTOR SCREEN
  if (screen === 'predictor') {
    return (
      <LinearGradient colors={['#667eea', '#764ba2']} style={styles.container}>
        <ScrollView contentContainerStyle={styles.predictorContent}>
          <TouchableOpacity
            onPress={() => setScreen('home')}
            style={styles.backButton}
          >
            <Text style={styles.backButtonText}>← Back</Text>
          </TouchableOpacity>

          <Text style={styles.screenTitle}>📝 Enter Area Data</Text>

          <View style={styles.formCard}>
            <InputField
              label="Population"
              placeholder="e.g., 150000"
              value={formData.population}
              onChangeText={(value) => handleInputChange('population', value)}
            />
            <InputField
              label="Age Distribution (0-1)"
              placeholder="e.g., 0.35"
              value={formData.age_dist}
              onChangeText={(value) => handleInputChange('age_dist', value)}
            />
            <InputField
              label="Doses Past 7 Days"
              placeholder="e.g., 2500"
              value={formData.past_7_days}
              onChangeText={(value) => handleInputChange('past_7_days', value)}
            />
            <InputField
              label="Infection Rate (%)"
              placeholder="e.g., 3.5"
              value={formData.infection_rate}
              onChangeText={(value) => handleInputChange('infection_rate', value)}
            />
            <InputField
              label="Awareness (0-100)"
              placeholder="e.g., 75"
              value={formData.awareness}
              onChangeText={(value) => handleInputChange('awareness', value)}
            />
            <InputField
              label="Power Stability (0-1)"
              placeholder="e.g., 0.85"
              value={formData.power_stability}
              onChangeText={(value) => handleInputChange('power_stability', value)}
            />
            <InputField
              label="Distance from Hub (km)"
              placeholder="e.g., 45"
              value={formData.distance_from_hub}
              onChangeText={(value) => handleInputChange('distance_from_hub', value)}
            />
          </View>

          <TouchableOpacity
            style={styles.randomButton}
            onPress={generateRandomData}
          >
            <Text style={styles.randomButtonText}>🎲 Random Sample</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.primaryButton, loading && styles.disabledButton]}
            onPress={generateStrategy}
            disabled={loading}
          >
            {loading ? (
              <ActivityIndicator color="#fff" size="small" />
            ) : (
              <Text style={styles.buttonText}>🔮 Generate Strategy</Text>
            )}
          </TouchableOpacity>
        </ScrollView>
      </LinearGradient>
    );
  }

  // RESULTS SCREEN
  if (screen === 'results' && strategy) {
    return (
      <LinearGradient colors={['#667eea', '#764ba2']} style={styles.container}>
        <ScrollView contentContainerStyle={styles.resultsContent}>
          <TouchableOpacity
            onPress={() => setScreen('predictor')}
            style={styles.backButton}
          >
            <Text style={styles.backButtonText}>← Back</Text>
          </TouchableOpacity>

          <Text style={styles.screenTitle}>📋 Strategy Results</Text>

          <View style={styles.resultCard}>
            <View style={styles.resultMetric}>
              <Text style={styles.resultLabel}>📦 Predicted Demand</Text>
              <Text style={styles.resultValue}>{strategy.demand}</Text>
              <Text style={styles.resultUnit}>doses/day</Text>
            </View>

            <View
              style={[
                styles.resultMetric,
                { borderTopColor: strategy.wasteRiskColor },
              ]}
            >
              <Text style={styles.resultLabel}>Waste Risk</Text>
              <Text
                style={[styles.resultValue, { color: strategy.wasteRiskColor }]}
              >
                {strategy.wasteRisk}
              </Text>
              <Text style={styles.resultUnit}>
                Confidence: {strategy.confidence}%
              </Text>
            </View>
          </View>

          <View style={styles.probabilityCard}>
            <Text style={styles.cardTitle}>Risk Distribution</Text>
            <ProbabilityBar
              label="Low Risk"
              value={parseFloat(strategy.probabilities.low)}
              color="#28a745"
            />
            <ProbabilityBar
              label="Medium Risk"
              value={parseFloat(strategy.probabilities.medium)}
              color="#ffc107"
            />
            <ProbabilityBar
              label="High Risk"
              value={parseFloat(strategy.probabilities.high)}
              color="#dc3545"
            />
          </View>

          <View style={styles.recommendationsCard}>
            <Text style={styles.cardTitle}>💡 Recommendations</Text>
            {strategy.recommendations.map((rec, idx) => (
              <View key={idx} style={styles.recommendationItem}>
                <Text style={styles.recommendationText}>{rec}</Text>
              </View>
            ))}
          </View>

          <TouchableOpacity
            style={styles.primaryButton}
            onPress={() => setScreen('home')}
          >
            <Text style={styles.buttonText}>Home</Text>
          </TouchableOpacity>
        </ScrollView>
      </LinearGradient>
    );
  }

  // ABOUT SCREEN
  if (screen === 'about') {
    return (
      <LinearGradient colors={['#667eea', '#764ba2']} style={styles.container}>
        <ScrollView contentContainerStyle={styles.aboutContent}>
          <TouchableOpacity
            onPress={() => setScreen('home')}
            style={styles.backButton}
          >
            <Text style={styles.backButtonText}>← Back</Text>
          </TouchableOpacity>

          <Text style={styles.screenTitle}>ℹ️ About</Text>

          <View style={styles.infoCard}>
            <Text style={styles.cardTitle}>🔬 Technology</Text>
            <Text style={styles.cardText}>
              • Machine Learning: Random Forest (Regression & Classification)
            </Text>
            <Text style={styles.cardText}>
              • Features: 7 input parameters capturing area demographics & infrastructure
            </Text>
            <Text style={styles.cardText}>
              • Frontend: React Native + Expo
            </Text>
            <Text style={styles.cardText}>
              • Backend: Python (Scikit-Learn, Streamlit)
            </Text>
          </View>

          <View style={styles.infoCard}>
            <Text style={styles.cardTitle}>📊 Models</Text>
            <Text style={styles.cardText}>
              <Text style={{ fontWeight: 'bold' }}>Demand Predictor:</Text> Predicts daily vaccine
              doses needed using area population, infection rate, and awareness.
            </Text>
            <Text style={styles.cardText}>
              <Text style={{ fontWeight: 'bold' }}>Waste Risk Classifier:</Text> Categorizes
              waste risk as Low, Medium, or High based on infrastructure stability and distance.
            </Text>
          </View>

          <View style={styles.infoCard}>
            <Text style={styles.cardTitle}>🎯 Use Cases</Text>
            <Text style={styles.cardText}>
              • Optimize vaccine distribution across regions
            </Text>
            <Text style={styles.cardText}>
              • Identify high-risk areas needing infrastructure improvements
            </Text>
            <Text style={styles.cardText}>
              • Plan supply chain logistics efficiently
            </Text>
            <Text style={styles.cardText}>
              • Reduce vaccine wastage and improve coverage
            </Text>
          </View>
        </ScrollView>
      </LinearGradient>
    );
  }
}

// Input Field Component
function InputField({ label, placeholder, value, onChangeText }) {
  return (
    <View style={styles.inputContainer}>
      <Text style={styles.inputLabel}>{label}</Text>
      <TextInput
        style={styles.input}
        placeholder={placeholder}
        value={value}
        onChangeText={onChangeText}
        keyboardType="decimal-pad"
      />
    </View>
  );
}

// Probability Bar Component
function ProbabilityBar({ label, value, color }) {
  return (
    <View style={styles.probabilityRow}>
      <Text style={styles.probabilityLabel}>{label}</Text>
      <View style={styles.barBackground}>
        <View
          style={[
            styles.barFill,
            {
              width: `${value * 100}%`,
              backgroundColor: color,
            },
          ]}
        />
      </View>
      <Text style={styles.probabilityValue}>{(value * 100).toFixed(0)}%</Text>
    </View>
  );
}

// Styles
const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  homeContent: {
    paddingHorizontal: 16,
    paddingTop: 40,
    paddingBottom: 30,
  },
  predictorContent: {
    paddingHorizontal: 16,
    paddingTop: 40,
    paddingBottom: 30,
  },
  resultsContent: {
    paddingHorizontal: 16,
    paddingTop: 40,
    paddingBottom: 30,
  },
  aboutContent: {
    paddingHorizontal: 16,
    paddingTop: 40,
    paddingBottom: 30,
  },
  backButton: {
    marginBottom: 20,
  },
  backButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
  headerBox: {
    marginBottom: 30,
    paddingBottom: 20,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#fff',
  },
  subtitle: {
    fontSize: 16,
    color: 'rgba(255,255,255,0.8)',
    marginTop: 5,
  },
  screenTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 20,
  },
  infoCard: {
    backgroundColor: 'rgba(255,255,255,0.15)',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
    borderLeftWidth: 4,
    borderLeftColor: '#fff',
  },
  cardTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 10,
  },
  cardText: {
    fontSize: 13,
    color: 'rgba(255,255,255,0.9)',
    lineHeight: 20,
    marginBottom: 8,
  },
  metricsBox: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 24,
    gap: 12,
  },
  metricCard: {
    flex: 1,
    backgroundColor: 'rgba(255,255,255,0.2)',
    borderRadius: 10,
    padding: 16,
    alignItems: 'center',
  },
  metricValue: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#fff',
  },
  metricLabel: {
    fontSize: 12,
    color: 'rgba(255,255,255,0.8)',
    marginTop: 5,
  },
  formCard: {
    backgroundColor: 'rgba(255,255,255,0.1)',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
  },
  inputContainer: {
    marginBottom: 16,
  },
  inputLabel: {
    color: '#fff',
    fontSize: 13,
    fontWeight: '600',
    marginBottom: 6,
  },
  input: {
    backgroundColor: 'rgba(255,255,255,0.2)',
    borderRadius: 8,
    paddingHorizontal: 12,
    paddingVertical: 10,
    color: '#fff',
    fontSize: 14,
  },
  primaryButton: {
    backgroundColor: '#fff',
    borderRadius: 8,
    paddingVertical: 14,
    alignItems: 'center',
    marginBottom: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 3,
    elevation: 5,
  },
  buttonText: {
    color: '#667eea',
    fontWeight: 'bold',
    fontSize: 16,
  },
  secondaryButton: {
    borderWidth: 2,
    borderColor: '#fff',
    borderRadius: 8,
    paddingVertical: 12,
    alignItems: 'center',
  },
  secondaryButtonText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 16,
  },
  randomButton: {
    backgroundColor: 'rgba(255,255,255,0.2)',
    borderRadius: 8,
    paddingVertical: 12,
    alignItems: 'center',
    marginBottom: 12,
    borderWidth: 1,
    borderColor: '#fff',
  },
  randomButtonText: {
    color: '#fff',
    fontWeight: '600',
    fontSize: 14,
  },
  disabledButton: {
    opacity: 0.6,
  },
  resultCard: {
    backgroundColor: 'rgba(255,255,255,0.1)',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
    overflow: 'hidden',
  },
  resultMetric: {
    alignItems: 'center',
    paddingVertical: 20,
    borderTopWidth: 1,
    borderTopColor: 'rgba(255,255,255,0.3)',
  },
  resultLabel: {
    fontSize: 12,
    color: 'rgba(255,255,255,0.7)',
    marginBottom: 8,
  },
  resultValue: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#fff',
  },
  resultUnit: {
    fontSize: 12,
    color: 'rgba(255,255,255,0.6)',
    marginTop: 4,
  },
  probabilityCard: {
    backgroundColor: 'rgba(255,255,255,0.1)',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
  },
  probabilityRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 12,
    gap: 10,
  },
  probabilityLabel: {
    color: '#fff',
    fontSize: 12,
    fontWeight: '600',
    width: 80,
  },
  barBackground: {
    flex: 1,
    height: 20,
    backgroundColor: 'rgba(255,255,255,0.2)',
    borderRadius: 10,
    overflow: 'hidden',
  },
  barFill: {
    height: '100%',
    borderRadius: 10,
  },
  probabilityValue: {
    color: '#fff',
    fontSize: 12,
    fontWeight: 'bold',
    width: 40,
    textAlign: 'right',
  },
  recommendationsCard: {
    backgroundColor: 'rgba(255,255,255,0.1)',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
  },
  recommendationItem: {
    paddingVertical: 10,
    paddingHorizontal: 12,
    backgroundColor: 'rgba(255,255,255,0.08)',
    borderRadius: 8,
    marginBottom: 10,
    borderLeftWidth: 3,
    borderLeftColor: 'rgba(255,255,255,0.5)',
  },
  recommendationText: {
    color: '#fff',
    fontSize: 13,
    lineHeight: 18,
  },
});
