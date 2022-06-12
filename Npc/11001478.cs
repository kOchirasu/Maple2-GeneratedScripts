using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001478: Ereve
/// </summary>
public class _11001478 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0106111607005759$
    // - $MyPCName$, what brings you to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0106111607005762$
                // - This $map:52010007$ has opened by the power of the Lumenstone in the Sanctuary of Light, somewhere in Nazkar Temple.
                switch (selection) {
                    // $script:0106111607005763$
                    // - What should I do now?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0106111607005764$
                // - There's only one thing to do. You must retrieve the Lumenstone before its chaotic light is consumed by darkness.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
