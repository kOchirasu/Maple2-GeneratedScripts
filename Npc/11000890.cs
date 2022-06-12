using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000890: Ringling
/// </summary>
public class _11000890 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003254$
    // - What is it? What is it? What is it? There has to be a reason...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003256$
                // - What brings you here?
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
