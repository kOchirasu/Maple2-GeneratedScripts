using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004485: Gracilis
/// </summary>
public class _11004485 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;30
    }

    protected override int Select() {
        // Select 0:
        // $script:1227192907012266$
        // - Those clothes... You're from Maple World, like me! You must be the first friendly face I've seen in days.
        // Select 20:
        // $script:0104144307012585$
        // - Hm...
        // TODO: 0,20
        return 0;
    }

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012267$
                // - Those clothes... You're from Maple World, like me! You must be the first friendly face I've seen in days.
                switch (selection) {
                    // $script:1227192907012268$
                    // - How's the research going?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012269$
                // - It's going... slowly. I can't stop thinking about this machine here...
                return 11;
            case (11, 1):
                // $script:1227192907012270$
                // - In design, it resembles the noblest of tools, the humble drill. You can see why I've become obsessed with it.
                return 11;
            case (11, 2):
                // $script:1227192907012271$
                // - But this is no ordinary drill, if it even is a drill at all. It seems like it can absorb energy of a certain wavelength. The same wavelength that aetherine resonates at, in fact.
                return 11;
            case (11, 3):
                // $script:1227192907012272$
                // - Perhaps it is used to mine for aetherine, then transmit the energy somehow? That's my hypothesis, at any rate.
                switch (selection) {
                    // $script:0114163707012712$
                    // - Amazing!
                    case 0:
                        return 70;
                }
                return -1;
            case (30, 0):
                // $script:0104144307012586$
                // - Yes, yes. I'm sure I've seen your face somewhere before. I'm really much too busy just now, though, so...
                switch (selection) {
                    // $script:0104144307012587$
                    // - What are you up to?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0104144307012588$
                // - An amateur academic. Of course. I suppose I can spare a minute of my time to explain.
                return 40;
            case (40, 1):
                // $script:0104144307012589$
                // - I am one of the premier mechanical engineers of Victoria Island! I snuck aboard—I mean, I legitimately boarded Sky Fortress in order to study the machines of Kritias.
                return 40;
            case (40, 2):
                // $script:0104144307012590$
                // - And look! I have discovered the most wonderful drills!
                return 40;
            case (40, 3):
                // $script:0104144307012591$
                // - At least, it looks like a drill. Technically speaking, that's not quite right.
                return 40;
            case (40, 4):
                // $script:0104144307012592$
                // - The structure of this drill defies all known convention—it's no twist drill, nor straight shank drill, nor step drill, and so forth.
                return 40;
            case (40, 5):
                // $script:0104144307012593$
                // - And this material! They've somehow found something better than cemented carbide. I can't even— I mean, it's just not—
                return 40;
            case (40, 6):
                // $script:0104144307012594$
                // - GASP! Sorry... I got so excited, I forgot to breathe.
                return 40;
            case (40, 7):
                // $script:0104144307012595$
                // - Anyway, it's all clear now, is it not?
                switch (selection) {
                    // $script:0104144307012596$
                    // - Not in the slightest.
                    case 0:
                        return 50;
                }
                return -1;
            case (50, 0):
                // $script:0104144307012597$
                // - You jest. I explained it clearly enough for a five-year-old to understand.
                switch (selection) {
                    // $script:0104144307012598$
                    // - Then I must be four.
                    case 0:
                        return 60;
                }
                return -1;
            case (60, 0):
                // $script:0104144307012599$
                // - ...
                return 60;
            case (60, 1):
                // $script:0104144307012600$
                // - You tire me. Shoo.
                return 60;
            case (60, 2):
                // $script:0104144307012601$
                // - But what is this drill for...?
                return -1;
            case (70, 0):
                // $script:0114163707012714$
                // - There's no shortage of amazing things in Kritias. That's why I'm so busy with research!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Next,
            (11, 2) => NpcTalkButton.Next,
            (11, 3) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Next,
            (40, 3) => NpcTalkButton.Next,
            (40, 4) => NpcTalkButton.Next,
            (40, 5) => NpcTalkButton.Next,
            (40, 6) => NpcTalkButton.Next,
            (40, 7) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.Next,
            (60, 1) => NpcTalkButton.Next,
            (60, 2) => NpcTalkButton.Close,
            (70, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
