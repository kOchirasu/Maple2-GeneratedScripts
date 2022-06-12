using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004022: Mysterious Bladesman
/// </summary>
public class _11004022 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614185307010031$
    // - Don't talk to me.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614185307010032$
                // - Go away, you bother me.
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
