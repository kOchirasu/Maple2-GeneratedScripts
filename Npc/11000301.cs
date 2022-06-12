using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000301: Jax
/// </summary>
public class _11000301 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001194$
    // - What brings you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001196$
                // - This place is dangerous. Be careful, especially if you want to use skills while on the Bone Bridge. Things can get scary there pretty quickly.
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
