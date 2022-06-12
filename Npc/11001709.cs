using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001709: Tinchai
/// </summary>
public class _11001709 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006961$
    // - Mm? Do you have something to say?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0728024507006989$
                // - I think there's more going on here than we realize. It's at times like this we have to keep a clear head. Got it?
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
