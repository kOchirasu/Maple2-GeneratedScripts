using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003872: Bedd
/// </summary>
public class _11003872 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0417135107009860$
    // - What's more important? The process? Or the results?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0417135107009861$
                // - I guess you need good process <i>and</i> solid results.
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
