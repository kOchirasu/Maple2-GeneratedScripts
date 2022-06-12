using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000047: Anna
/// </summary>
public class _11000047 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000215$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000218$
                // - I used to love hearing the sound of bow craftsmen carving wood. The most talented of them all was Freeman. 
                return 30;
            case (30, 1):
                // $script:0831180407000219$
                // - He was $npcName:11000007[gender:1]$'s father. It's a shame an illness took him so early, but he would surely approve of the woman his daughter grew to be.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
