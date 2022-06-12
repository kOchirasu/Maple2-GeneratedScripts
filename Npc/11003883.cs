using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003883: Beatrice
/// </summary>
public class _11003883 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0515102507009915$
    // - Welcome, my other half.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0515102507009916$
                // - My kin... you've come.
                return -1;
            case (30, 0):
                // $script:0515102507009917$
                // - Prove that I made the right decision, $MyPCName$.
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
