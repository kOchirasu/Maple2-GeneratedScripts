using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003888: Celine
/// </summary>
public class _11003888 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0515102507009930$
    // - Listen closely to the waves. Can you hear the voice of the ocean?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0515102507009931$
                // - Listen closely to the waves. Can you hear the voice of the ocean?
                return -1;
            case (30, 0):
                // $script:0515102507009932$
                // - I'm sure you can quiet the angry seas.
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
