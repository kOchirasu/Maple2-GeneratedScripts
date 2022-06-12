using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000649: Prisoner 170121
/// </summary>
public class _11000649 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180407002656$
    // - What are you looking at?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002660$
                // - Another tourist? Come to see all the animals in their cages?
                switch (selection) {
                    // $script:0831180407002661$
                    // - How did you end up in here?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002662$
                // - I swore, and apparently that's SO wrong that they had to throw me into prison?
                return -1;
            case (50, 0):
                // $script:1211023307004934$
                // - Another tourist? Come to see all the animals in their cages?
                switch (selection) {
                    // $script:1211023307004935$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:1211023307004936$
                // - No. Get lost.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
