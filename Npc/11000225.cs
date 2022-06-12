using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000225: Old Man Maneux
/// </summary>
public class _11000225 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000979$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000982$
                // - Love isn't just about being with someone. Sometimes it's about their memory, too...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
