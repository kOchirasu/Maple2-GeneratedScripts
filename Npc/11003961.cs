using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003961: Heavy Gunner
/// </summary>
public class _11003961 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614143707010013$
    // - Booooring.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614143707010014$
                // - Do you want me to teach you about the immense power of the lapenshards? ...No? Pfft.
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
