using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000223: Morris
/// </summary>
public class _11000223 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000973$
    // - Are you here to talk to me? But why?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000975$
                // - I don't understand women. It feels like they're always changing their minds. 
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
