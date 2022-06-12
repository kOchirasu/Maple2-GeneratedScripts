using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001234: Ryder
/// </summary>
public class _11001234 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1125194807004482$
    // - Have you seen anyone out of place?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1125194807004485$
                // - $npc:11001231[gender:0]$ hurt dozens of us when he escaped last night. We all knew we didn't stand a chance, but what else could we do? I'm in no shape to help bring him in, but at least I can keep a lookout.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
