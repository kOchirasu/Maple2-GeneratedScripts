using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003963: Runeblade
/// </summary>
public class _11003963 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614143707010017$
    // - Are you versed in the way of the blade?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614143707010018$
                // - I'd be grateful for the opportunity to speak with a peer...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
