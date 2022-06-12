using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004147: Ralph
/// </summary>
public class _11004147 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010565$
    // - What do you want?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010566$
                // - This place is gonna make me rich! I've just gotta figure out how, first...
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
