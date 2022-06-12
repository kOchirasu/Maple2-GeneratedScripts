using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004176: Lennon
/// </summary>
public class _11004176 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010614$
    // - It's good to see you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010615$
                // - When things get dicey, it's good to have somebody who's got your back.
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
