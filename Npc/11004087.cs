using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004087: Cheeky Frog
/// </summary>
public class _11004087 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0622133907010298$
    // - Ribbit ribbit!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0622133907010299$
                // - Ribbit ribbit!
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
