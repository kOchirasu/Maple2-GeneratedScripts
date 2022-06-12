using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004142: Merin
/// </summary>
public class _11004142 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010555$
    // - Wow!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010556$
                // - My favorite game is hide-and-seek!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
