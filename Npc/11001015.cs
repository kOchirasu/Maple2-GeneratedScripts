using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001015: Yena
/// </summary>
public class _11001015 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003459$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003462$
                // - Each magic-user has their own spell. I haven't chosen mine yet. Alio olio! Hoi, hoi! Chacharachat! Which one sounds the best to you?
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
