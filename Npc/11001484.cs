using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001484: Lilia
/// </summary>
public class _11001484 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0201104307005858$
    // - Did you come to see me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0201104307005861$
                // - Do you want to know about the events we're running right now? Feel free to ask me all about 'em!
                return 30;
            case (30, 1):
                // $script:0201104607005858$
                // - If I have any info to share about events, I'll let you know.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
