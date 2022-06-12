using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001122: Velte
/// </summary>
public class _11001122 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0910171307003829$
    // - Do you have business with me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0910171307003832$
                // - Good day. My name is $npcName:11001122[gender:0]$, and I'm a member of the Wall Climbers. We're a group that supports each other as we work to climb every wall we can find. If you have a passion for climbing, we're right there with you!
                switch (selection) {
                    // $script:0910171307003833$
                    // - You look a little different from the other Wall Climbers.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0910171307003834$
                // - Really? How so? 
                switch (selection) {
                    // $script:0910171307003835$
                    // - Are you sure you're a Wall Climber?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0910171307003836$
                // - ...Sheesh, can't you just let it go? If you're going to keep asking stupid questions, I don't want to talk to you.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
