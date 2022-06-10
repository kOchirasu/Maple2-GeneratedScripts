using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004485: Gracilis
/// </summary>
public class _11004485 : NpcScript {
    internal _11004485(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012266$ 
                // - Those clothes... You're from Maple World, like me! You must be the first friendly face I've seen in days. 
                return true;
            case 20:
                // $script:0104144307012585$ 
                // - Hm... 
                return true;
            case 10:
                // $script:1227192907012267$ 
                // - Those clothes... You're from Maple World, like me! You must be the first friendly face I've seen in days. 
                switch (selection) {
                    // $script:1227192907012268$
                    // - How's the research going?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012269$ 
                // - It's going... slowly. I can't stop thinking about this machine here... 
                // $script:1227192907012270$ 
                // - In design, it resembles the noblest of tools, the humble drill. You can see why I've become obsessed with it. 
                // $script:1227192907012271$ 
                // - But this is no ordinary drill, if it even is a drill at all. It seems like it can absorb energy of a certain wavelength. The same wavelength that aetherine resonates at, in fact. 
                // $script:1227192907012272$ 
                // - Perhaps it is used to mine for aetherine, then transmit the energy somehow? That's my hypothesis, at any rate. 
                switch (selection) {
                    // $script:0114163707012712$
                    // - Amazing!
                    case 0:
                        Id = 70;
                        return false;
                }
                return true;
            case 30:
                // $script:0104144307012586$ 
                // - Yes, yes. I'm sure I've seen your face somewhere before. I'm really much too busy just now, though, so... 
                switch (selection) {
                    // $script:0104144307012587$
                    // - What are you up to?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0104144307012588$ 
                // - An amateur academic. Of course. I suppose I can spare a minute of my time to explain. 
                // $script:0104144307012589$ 
                // - I am one of the premier mechanical engineers of Victoria Island! I snuck aboard—I mean, I legitimately boarded Sky Fortress in order to study the machines of Kritias. 
                // $script:0104144307012590$ 
                // - And look! I have discovered the most wonderful drills! 
                // $script:0104144307012591$ 
                // - At least, it looks like a drill. Technically speaking, that's not quite right. 
                // $script:0104144307012592$ 
                // - The structure of this drill defies all known convention—it's no twist drill, nor straight shank drill, nor step drill, and so forth. 
                // $script:0104144307012593$ 
                // - And this material! They've somehow found something better than cemented carbide. I can't even— I mean, it's just not— 
                // $script:0104144307012594$ 
                // - GASP! Sorry... I got so excited, I forgot to breathe. 
                // $script:0104144307012595$ 
                // - Anyway, it's all clear now, is it not? 
                switch (selection) {
                    // $script:0104144307012596$
                    // - Not in the slightest.
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 50:
                // $script:0104144307012597$ 
                // - You jest. I explained it clearly enough for a five-year-old to understand. 
                switch (selection) {
                    // $script:0104144307012598$
                    // - Then I must be four.
                    case 0:
                        Id = 60;
                        return false;
                }
                return true;
            case 60:
                // $script:0104144307012599$ 
                // - ... 
                // $script:0104144307012600$ 
                // - You tire me. Shoo. 
                // $script:0104144307012601$ 
                // - But what is this drill for...? 
                return true;
            case 70:
                // $script:0114163707012714$ 
                // - There's no shortage of amazing things in Kritias. That's why I'm so busy with research! 
                return true;
            default:
                return true;
        }
    }
}
