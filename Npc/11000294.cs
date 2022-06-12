using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000294: Papa Frog
/// </summary>
public class _11000294 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407001171$
    // - May I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407001175$
                // - Croak, croak, croak. Croaaaaakkk...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
