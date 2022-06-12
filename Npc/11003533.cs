using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003533: Veliche
/// </summary>
public class _11003533 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1126155107011958$
    // - The future is in our hands.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1126155107011959$
                // - Speak. I'm listening.
                switch (selection) {
                    // $script:1126155107011960$
                    // - Tell me about Tria's navy.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1126155107011961$
                // - After all this time, you haven't seen the famous navy of Tria?
                return 31;
            case (31, 1):
                // $script:1126155107011962$
                // - I suppose that's not unreasonable. Tria's navy isn't in Tria at the moment, after all.
                return 31;
            case (31, 2):
                // $script:1126155107011963$
                // - A few months before the empress's grand court, the main fleet was dispatched to an island far away. Not even I know where the command came from.
                return 31;
            case (31, 3):
                // $script:1126155107011964$
                // - Fa—I mean, Admiral Martini didn't even take the time to tell me about the mission. They simply set sail, leaving myself and a few petty officers to command a skeleton fleet.
                return 31;
            case (31, 4):
                // $script:1126155107011965$
                // - They don't appear on Sky Fortress's radar, either. I'm not sure what to make of the bulk of our military vanishing at a time like this...
                return 31;
            case (31, 5):
                // $script:1126155107011966$
                // - I wonder if he's even still alive...
                return 31;
            case (31, 6):
                // $script:1126155107011967$
                // - I've said too much. You can trust in Tria's naval forces. The entire empire is under my personal protection.
                return -1;
            case (40, 0):
                // $script:1126155107011968$
                // - Prove yourself to my officers, and I'll consider entrusting you with a mission for the Maple Alliance.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Next,
            (31, 2) => NpcTalkButton.Next,
            (31, 3) => NpcTalkButton.Next,
            (31, 4) => NpcTalkButton.Next,
            (31, 5) => NpcTalkButton.Next,
            (31, 6) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
