using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003884: Pemberton
/// </summary>
public class _11003884 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0515102507009918$
    // - Hmm...
    //   My duty is to look after lady $npcName:11003883[gender:0]$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0515102507009919$
                // - I will not forgive those who would dishonor my lady!
                return -1;
            case (30, 0):
                // $script:0515102507009920$
                // - This is the first time I've seen $npcName:11003883[gender:0]$ so active. Whether or not this goes on depends on $MyPCName$'s role.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
