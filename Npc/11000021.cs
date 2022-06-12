using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000021: Santiago
/// </summary>
public class _11000021 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;40
    }

    // Select 0:
    // $script:0831180407000106$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000107$
                // - My grandson is so rebellious that he's going to give me a heart attack. I miss the days when he would just listen.
                return -1;
            case (40, 0):
                // $script:0831180407000110$
                // - $npcName:11000054[gender:0]$ is as stubborn as a mule. Please find him before he leaves $map:63000001$.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
