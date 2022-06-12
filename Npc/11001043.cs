using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001043: Aiden
/// </summary>
public class _11001043 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003561$
    // - This is an emergency. Whatever business you have, it can wait. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003564$
                // - Real pros always know what to do, no matter how dire the situation is.
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
