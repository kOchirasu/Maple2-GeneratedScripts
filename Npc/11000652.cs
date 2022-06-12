using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000652: Prisoner 170124
/// </summary>
public class _11000652 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180407002677$
    // - When can I get out of here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002681$
                // - Nine thousand nine hundred fifty-five... Nine thousand nine hundred fifty-six...
                switch (selection) {
                    // $script:0831180407002682$
                    // - What are you doing?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002683$
                // - Are you blind? I'm working! I have to pull a million weeds to have my sentence reduced. Argh, and now you've made me lose count!
                return -1;
            case (50, 0):
                // $script:1210061907004926$
                // - Nine thousand nine hundred fifty-five... Nine thousand nine hundred fifty-six...
                switch (selection) {
                    // $script:1210061907004927$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:1210061907004928$
                // - ...Nine thousand nine hundred six... Drat! You made me lose count!
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
